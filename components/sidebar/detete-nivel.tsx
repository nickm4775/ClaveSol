import React, { useEffect, useState } from "react";
import {Modal, ModalContent, ModalHeader, ModalBody, ModalFooter, Button, useDisclosure,Link, Select, SelectItem} from "@nextui-org/react";
 
interface Nivel {
  id: number;
  nombre: string;
  requisitos: Requisito[];
}

interface Requisito{
  id:number;
  nombre: string;
  permanecer:boolean;
  subir: boolean;
}

export default function DeleteIcon() {
  const {isOpen, onOpen, onOpenChange} = useDisclosure();
  const [levels, setLevels] = useState<Nivel[]>([]);
  const [levelNames, setLevelNames]= useState<Nivel[]>([]);
  const [efectoEjecutado , setefectoEjecutado]= useState<boolean>(false);
  const [nivSel, setnivSel]= useState<number>();


  useEffect(() => {
    const fetchLevels = async () => {
      try {
        const response = await fetch('http://127.0.0.1:8000/ClaveDeSol/Nivel/Nivel');
        if (response.ok) {
          const data = await response.json();
           
          if (Array.isArray(data.results.Nivel)) {
            setLevels(data.results.Nivel);
            const levelNamesFromData = data.results.Nivel.map((level: Nivel) => level.nombre);
            setLevelNames(levelNamesFromData);
            
          } else {
            console.error('Error: Data is not an array');
          }
        } else {
          console.error('Error fetching levels:', response.status);
        }
      } catch (error) {
        console.error(error);
      }
    };

    fetchLevels();
  }, []);
  const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();

    try {
      
      const response = await fetch(`http://127.0.0.1:8000/ClaveDeSol/Nivel/DeleteNivel/${nivSel}`, {
        method: 'DELETE',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({}),
      });
      const data = await response.json();
      
      
     

      window.alert('Nivel eliminado correctamente');
      window.location.reload();
    } catch (error) {
      console.error('Error al eliminar el nivel:', error);
    }
  };

  return (
    <>

    
      <Link onPress={onOpen} color="danger">Eliminar Nivel</Link>

      <Modal 
        backdrop="opaque" 
        isOpen={isOpen} 
        onOpenChange={onOpenChange}
        classNames={{
          backdrop: "bg-gradient-to-t from-zinc-900 to-zinc-900/10 backdrop-opacity-20"
        }}
      >
        <form onSubmit={handleSubmit}>
        <ModalContent>
          {(onClose) => (
            <>
              <ModalHeader className="flex flex-col gap-1">Eliminar Nivel</ModalHeader>
             
              <ModalBody>
                <p> 
                  Seleccione el nivel que desee eliminar
                </p>
                <Select
      label="Nivel"
      placeholder="Selecione el requisito que desea eliminar"
      onChange={(e)=> { const selectedIdsString = e.target.value;
        const idsArrayAsString = selectedIdsString.split(',');
        const idsArrayAsNumbers = idsArrayAsString.map(id => Number(id.trim()));
        const nivelesFiltradosPorId = levels.filter(nivel => idsArrayAsNumbers.includes(nivel.id));
        
        // Aquí asumimos que quieres seleccionar el primer nivel que coincida con los IDs ingresados
        if (nivelesFiltradosPorId.length > 0) {
          setnivSel(nivelesFiltradosPorId[0].id); // Guarda el ID del primer nivel filtrado
        } 
        console.log("nivel Seleccionado ", nivSel);
        
      }}
      selectionMode="multiple"
      className="max-w-xs w-full flex  text-default-500 hover:text-default-900 transition-colors"
    >
      {levels.map((nivel) => (
  <SelectItem key={nivel.id} value={nivel.id}>
    {nivel.nombre}
  </SelectItem>
))}
    </Select>
                
              </ModalBody>
              <ModalFooter>
                <Button color="danger" variant="light" onPress={onClose}>
                  Cerrar
                </Button>
                <Button color="success" type="submit" onPress={onClose}>
                  eliminar
                </Button>
              </ModalFooter>
            </>
          )}
        </ModalContent>
        </form>
     </Modal>
     
    </>
  );
}
