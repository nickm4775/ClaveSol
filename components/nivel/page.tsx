"use client";
import React, { useEffect, useState } from "react";
import {
  Table,
  TableHeader,
  TableColumn,
  TableBody,
  TableRow,
  TableCell,
  Input,
  Button,
  DropdownTrigger,
  Dropdown,
  DropdownMenu,
  DropdownItem,
  Chip,
  User,
  Pagination,
  Selection,
  ChipProps,
  SortDescriptor
} from "@nextui-org/react";
import {PlusIcon} from "./PlusIcon";
import {VerticalDotsIcon} from "./VerticalDotsIcon";
import {ChevronDownIcon} from "./ChevronDownIcon";
import {SearchIcon} from "./SearchIcon";
import {capitalize} from "./utils";
import {AddUser} from './add-Estudiante';
import {usenivelSelectStore} from '@/components/hooks/usenivelSelectStore';
import {useEstudianteStore} from "../hooks/useEstudiantes";
import { useRouter } from "next/navigation";
// const statusColorMap: Record<string, ChipProps["color"]> = {
//   true: "success",
//   false: "danger",
//   };
const columns = [
  {name: "ID", uid: "id", sortable: true},
  {name: "NOMBRE", uid: "nombre", sortable: true},
  {name: "APELLIDOS", uid: "apellidos", sortable: true},
  {name: "EMAIL", uid: "email"},
  {name: "REQUISITOS PARA PERMANECER", uid: "requisitospermanecer", sortable: true},
  {name: "REQUSITOS PARA SUBIR", uid: "requisitosubir"},
  {name: "REQUISITOS CUMPLIDOS", uid: "requisitoscumplidos", sortable: true},
  {name: "ACCIONES", uid: "acciones"},
];

interface Requisitos{
  id: number;
  nombre: string;
  permanecer: boolean;
  subir:boolean;
}
interface Estudiante{
  nivel: number;
  nivel_nombre: string;
  nombre: number;
  requisitos_cumplidos_permanecer: Requisitos[];
  requisitos_cumplidos_subir: Requisitos[];
  requisitos_cumplidos: Requisitos[];
  id: number;
  email: string;
  first_name:string;
  last_name:string;
  is_active:boolean;
  is_staff:boolean;
  is_coordinador:boolean;
  is_admin:boolean;
  is_estudiante:boolean;
  last_login: Date;
}



const INITIAL_VISIBLE_COLUMNS = ["nombre", "email", "requisitospermanecer", "requisitosubir","requisitoscumplidos","acciones"];



export default function Nivel() {
  const [filterValue, setFilterValue] = React.useState("");
  const [selectedKeys, setSelectedKeys] = React.useState<Selection>(new Set([]));
  const [visibleColumns, setVisibleColumns] = React.useState<Selection>(new Set(INITIAL_VISIBLE_COLUMNS));
  const [statusFilter, setStatusFilter] = React.useState<Selection>("all");
  const [rowsPerPage, setRowsPerPage] = React.useState(5);
  const [sortDescriptor, setSortDescriptor] = React.useState<SortDescriptor>({
    
    direction: "ascending",
  });
  const routes = useRouter();
  const [page, setPage] = React.useState(1);
  const [estudiantes, setEstudiantes]= useState<Estudiante[]>([]);
  const {students, addStudent,removeStudent,setAllStudents} = useEstudianteStore();

  
 
  const loadEstudiantes = () => {
    fetch('http://127.0.0.1:8000/ClaveDeSol/Estudiante/estudiantes/')
     .then(response => response.json())
     .then(data => {
        const nivelSeleccionado = usenivelSelectStore.getState().nivelData?.nombre;
        console.log("nivelsele", nivelSeleccionado);
        if (!nivelSeleccionado) {
          console.error('Nivel no seleccionado');
          return;
        }
        setAllStudents(data.estudiantes);
        console.log("todos estudiantes", useEstudianteStore.getState());
        const estudiantesFiltrados: Estudiante[] = useEstudianteStore.getState().students.filter((estudiantes: Estudiante) => estudiantes.nivel_nombre === nivelSeleccionado);
        setEstudiantes(estudiantesFiltrados); // Solo guarda los estudiantes que coincidan con el nivel seleccionado
      })
     .catch(error => console.error('Error al cargar los estudiantes:', error));
  };
  useEffect(() => {
    const unsubscribe = usenivelSelectStore.subscribe(() => {
      // Llama a las funciones necesarias aquí
      routes.refresh();
      loadEstudiantes();
    });
  
    // Asegúrate de limpiar la suscripción cuando el componente se desmonte
    return () => unsubscribe();
  }, []); // El arreglo vacío significa que este efecto se ejecutará solo una vez, similar a componentDidMount

  const hasSearchFilter = Boolean(filterValue);

  const headerColumns = React.useMemo(() => {
    if (visibleColumns === "all") return columns;

    return columns.filter((column) => Array.from(visibleColumns).includes(column.uid));
  }, [visibleColumns]);

  const filteredItems = React.useMemo(() => {
    let filteredUsers = [...estudiantes];

    if (hasSearchFilter) {
      filteredUsers = filteredUsers.filter((estudiante) =>
        estudiante.first_name.toLowerCase().includes(filterValue.toLowerCase()),
      );
    }
    if (statusFilter !== "all"  ) {
      filteredUsers = filteredUsers.filter((estudiante) =>
        estudiante.is_active? true : false,
      );
    }

    return filteredUsers;
  }, [estudiantes, filterValue, hasSearchFilter, statusFilter]);

  const pages = Math.ceil(filteredItems.length / rowsPerPage);

  const items = React.useMemo(() => {
    const start = (page - 1) * rowsPerPage;
    const end = start + rowsPerPage;

    return filteredItems.slice(start, end);
  }, [page, filteredItems, rowsPerPage]);

  const sortedItems = React.useMemo(() => {
    return [...items].sort((a: Estudiante, b: Estudiante) => {
      const first = a[sortDescriptor.column as keyof Estudiante] as number;
      const second = b[sortDescriptor.column as keyof Estudiante] as number;
      const cmp = first < second ? -1 : first > second ? 1 : 0;

      return sortDescriptor.direction === "descending" ? -cmp : cmp;
    });
  }, [sortDescriptor, items]);

  const renderCell = React.useCallback((estudiantes: Estudiante, columnKey: React.Key) => {
    const cellValue = estudiantes[columnKey as keyof Estudiante];

    switch (columnKey) {
      case "id":
        return (
          <p>
            {estudiantes.id}
          </p>
        );
      case "nombre":
        return (
          <p>
            {estudiantes.first_name}
          </p>
        );
        case "apellidos":
        return (
          <p>
            {estudiantes.last_name}
          </p>
        );
      case "email":
        return (
          <div className="flex flex-col">
            <p className="text-bold text-tiny capitalize text-default-400">{estudiantes.email}</p>
          </div>
        );
        case "requisitospermanecer":
        return (
          <div className="flex flex-col">
    {estudiantes.requisitos_cumplidos_permanecer.map((requisitos, index) => (
    <div key={index}>{`${requisitos}`}</div>
  ))}
  </div>
        );
        case "requisitosubir":
        return (
          <div className="flex flex-col">
    {estudiantes.requisitos_cumplidos_subir.map((requisito, index) => (
    <div key={index}>{`${requisito}`}</div>
  ))}
  </div>
        );
        case "requisitoscumplidos":
        return (
          <div className="flex flex-col">
    {estudiantes.requisitos_cumplidos_subir.map((requisito, index) => (
    <div key={index}>{`${requisito}`}</div>
  ))}
  </div>
        );
     
      case "acciones":
        return (
          <div className="relative flex justify-end items-center gap-2">
            <Dropdown>
              <DropdownTrigger>
                <Button isIconOnly size="sm" variant="light">
                  <VerticalDotsIcon className="text-default-300" />
                </Button>
              </DropdownTrigger>
              <DropdownMenu>
                <DropdownItem>Detalles</DropdownItem>
                <DropdownItem>Editar</DropdownItem>
                <DropdownItem>Borrar</DropdownItem>
              </DropdownMenu>
            </Dropdown>
          </div>
        );
      default:
        return <>{cellValue?.toString()}</>;
    }
  }, []);

  const onNextPage = React.useCallback(() => {
    if (page < pages) {
      setPage(page + 1);
    }
  }, [page, pages]);

  const onPreviousPage = React.useCallback(() => {
    if (page > 1) {
      setPage(page - 1);
    }
  }, [page]);

  const onRowsPerPageChange = React.useCallback((e: React.ChangeEvent<HTMLSelectElement>) => {
    setRowsPerPage(Number(e.target.value));
    setPage(1);
  }, []);

  const onSearchChange = React.useCallback((value?: string) => {
    if (value) {
      setFilterValue(value);
      setPage(1);
    } else {
      setFilterValue("");
    }
  }, []);

  const onClear = React.useCallback(()=>{
    setFilterValue("")
    setPage(1)
  },[])

  const topContent = React.useMemo(() => {
    return (    <div className=" w-full flex flex-col gap-4">
      <div className="flex flex-col gap-4">
        <div className="flex justify-between gap-3 items-end">
          <Input
            isClearable
            className="w-full sm:max-w-[44%]"
            placeholder="Busqueda por el nombre..."
            startContent={<SearchIcon />}
            value={filterValue}
            onClear={() => onClear()}
            onValueChange={onSearchChange}
          />
          <div className="flex gap-3">
            
            <Dropdown>
              <DropdownTrigger className="hidden sm:flex">
                <Button endContent={<ChevronDownIcon className="text-small" />} variant="flat">
                  Columnas
                </Button>
              </DropdownTrigger>
              <DropdownMenu
                disallowEmptySelection
                aria-label="Table Columns"
                closeOnSelect={false}
                selectedKeys={visibleColumns}
                selectionMode="multiple"
                onSelectionChange={setVisibleColumns}
              >
                {columns.map((column) => (
                  <DropdownItem key={column.uid} className="capitalize">
                    {capitalize(column.name)}
                  </DropdownItem>
                ))}
              </DropdownMenu>
            </Dropdown>
            <AddUser/>
          </div>
        </div>
        <div className="flex justify-between items-center">
          <span className="text-default-400 text-small">Total {estudiantes.length} estudiantes</span>
          <label className="flex items-center text-default-400 text-small">
            Columnas por página:
            <select
              className="bg-transparent outline-none text-default-400 text-small"
              onChange={onRowsPerPageChange}
            >
              <option value="5">5</option>
              <option value="10">10</option>
              <option value="15">15</option>
            </select>
          </label>
        </div>
      </div>
      </div>
    );
  }, [filterValue, onSearchChange, visibleColumns, estudiantes.length, onRowsPerPageChange, onClear]);

  const bottomContent = React.useMemo(() => {
    return (
      <div className="py-2 px-2 flex justify-between items-center">
        <span className="w-[30%] text-small text-default-400">
          {selectedKeys === "all"
            ? "Todos los estudiantes seleccionados"
            : `${selectedKeys.size} de ${filteredItems.length} seleccionados`}
        </span>
        <Pagination
          isCompact
          showControls
          showShadow
          color="success"
          page={page}
          total={pages}
          onChange={setPage}
        />
        <div className="hidden sm:flex w-[30%] justify-end gap-2">
          <Button isDisabled={pages === 1} size="sm" variant="flat" onPress={onPreviousPage}>
            Anterior
          </Button>
          <Button isDisabled={pages === 1} size="sm" variant="flat" onPress={onNextPage}>
            Siguiente
          </Button>
        </div>
      </div>
    );
  }, [selectedKeys, filteredItems.length, page, pages, onPreviousPage, onNextPage]);

  return (
    <Table
      isHeaderSticky
      bottomContent={bottomContent}
      bottomContentPlacement="outside"
      classNames={{
        wrapper: "max-h-[700px]",
      }}
      selectedKeys={selectedKeys}
      selectionMode="multiple"
      sortDescriptor={sortDescriptor}
      topContent={topContent}
      topContentPlacement="outside"
      onSelectionChange={setSelectedKeys}
      onSortChange={setSortDescriptor}
      color="success"
    >
      <TableHeader columns={headerColumns}>
        {(column) => (
          <TableColumn
            key={column.uid}
            align={column.uid === "actions" ? "center" : "start"}
            allowsSorting={column.sortable}
            
          >
            {column.name}
          </TableColumn>
        )}
      </TableHeader>
      <TableBody emptyContent={"No users found"} items={sortedItems}>
      {(item) => (
          <TableRow key={item.id}>
            {(columnKey) => <TableCell>{renderCell(item, columnKey)}</TableCell>}
          </TableRow>
        )}

        
      </TableBody>
    </Table>
  );
}
