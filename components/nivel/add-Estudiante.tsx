"use client"
import {
  Button,
  Input,
  Modal,
  ModalBody,
  ModalContent,
  ModalFooter,
  ModalHeader,
  useDisclosure,
  Select,
  SelectItem,
} from "@nextui-org/react";
import React, { useEffect, useState } from "react";
import { usenivelSelectStore } from "../hooks/usenivelSelectStore";


interface Nivel{
  id: number;
  nombre: string;
  requisitos: Requisitos[];
}

interface Requisitos{
  id: number;
  nombre: string;
  permanecer: boolean;
  subir:boolean;
}
interface User{
  
    
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
export const AddUser = () => {
  const { isOpen, onOpen, onOpenChange } = useDisclosure();
  const [Users, setUsers] = useState<User[]>([]);
  const [studentsSele, setStudentsSele] = useState<number>();
  const [requisitos, setRequisitos]= useState<Requisitos[]>([]);
  const [studentData, setstudentData] = useState<User>();;
  const [nivelSeleccionado, setnivelSeleccionado] = useState<number>();
  const [requisitossub, setrequisitossub] =useState<Requisitos[]>([]);
  const [requisitosmant, setrequisitosmant]= useState<Requisitos[]>([]);
  
  useEffect(() => {

       
    fetch('http://127.0.0.1:8000/ClaveDeSol/User/User')
       .then(response => response.json())
       .then(data => setUsers(data.results.User))
       .catch(error => console.error('Error fetching data: ', error));
       
       const nivelData = usenivelSelectStore.getState().nivelData;
       if (nivelData && nivelData.id !== undefined) {
           setnivelSeleccionado(nivelData.id);
           setrequisitossub(nivelData.requisitos.filter(requisito => requisito.subir) as Requisitos[]);
           setrequisitosmant(nivelData.requisitos.filter(requisito => requisito.permanecer)as Requisitos[]);
       }
}, []);


  const HandleSubmit = async () => {
    try {
            
      

      const response = await fetch('http://127.0.0.1:8000/ClaveDeSol/Estudiante/CreateEstudiante', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          // Incluye cualquier otro header necesario, como tokens de autenticación si es necesario
        },
        body: JSON.stringify({
       nivel : nivelSeleccionado,
       nombre : studentsSele,
       requisitos_cumplidos_permanecer: requisitosmant,
       requisitos_cumplidos_subir: requisitossub,
       requisitos_cumplidos: []

        }),
      });

      if (!response.ok) {
        throw new Error(`HTTP error status: ${response.status}`);
      }
  
      alert('Estudiante creado exitosamente');

    } catch (error) {
      console.error('Error al crear el estudiante:', error);
      alert('Hubo un error al crear el estudiante.');
    }
  };

  return (
    <div>
      <>
        <Button onPress={onOpen} color="success">
        Añadir Estudiante
        </Button>
        <Modal
          isOpen={isOpen}
          onOpenChange={onOpenChange}
          placement="top-center"
          
        >
          <form onSubmit={HandleSubmit}>
          <ModalContent>
            {(onClose) => (
              <>
                <ModalHeader className="flex flex-col gap-1">
                  Añadir Estudiante
                </ModalHeader>
                <ModalBody>
                <div className="flex w-full flex-wrap md:flex-nowrap gap-4">
      <Select 
        label="Selecciona un estudiante" 
        className="max-w-xs" 
        onChange={(e)=> setStudentsSele(Number(e.target.value))}
      >
        {Users.map((estudiante) => (
          <SelectItem key={estudiante.id} value={estudiante.id}>
            {estudiante.email}
          </SelectItem>
        ))}
      </Select>
      </div>
                </ModalBody>
                <ModalFooter>
                  <Button color="danger" variant="flat" onClick={onClose}>
                    Cerrar
                  </Button>
                  <Button color="success" onPress={onClose} type="submit">
                    Añadir Estudiante
                  </Button>
                </ModalFooter>
              </>
            )}
          </ModalContent>
          </form>
        </Modal>
      </>
    </div>
  );
};
