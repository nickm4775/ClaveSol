import {
    Button,
    Input,
    Modal,
    ModalBody,
    ModalContent,
    ModalFooter,
    ModalHeader,
    useDisclosure,
    Link,
    Image,
     } from "@nextui-org/react";
     import {Select, SelectSection, SelectItem} from "@nextui-org/select";
import { useRouter } from "next/navigation";
import React, {useState, useEffect} from "react";


  interface Nivel {
    id:number;
    nombre: string;
    requisitos: Requisito[];
  }

  interface Requisito{
    id:number;
    nombre: string;
    permanecer:boolean;
    subir: boolean;
  }
  
  export const AddNivel = () => {
    const { isOpen, onOpen, onOpenChange } = useDisclosure();
    const [requisitos, setRequisitos] = useState<Requisito[]>([]);
    const [reqSel, setreqSel]= useState<Requisito[]>([]);
    const [nivelName, setNivelName] = useState('');
    const routes = useRouter();
    const [efectoEjecutado , setefectoEjecutado]= useState<boolean>(false);
  
    useEffect(() => {
      if(!efectoEjecutado){
      const fetchRequisitos = async () => {
        try {
          const response = await fetch('http://127.0.0.1:8000/ClaveDeSol/Requisito/Requisito');
          if(response.ok){
            const data= await response.json()
            setRequisitos(data.results.Requisito);
            console.log(requisitos);
           const nombrereq = data.results.Requisito.map((requisitos: Requisito) => requisitos.nombre);
            setefectoEjecutado(true); 
          }
        } catch (error) {

          console.error('Error fetching requirements:', error);
        }
      };
      fetchRequisitos(),[]
   } });
  
  
   const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();

    try {
      setNivelName('');
      const response = await fetch('http://127.0.0.1:8000/ClaveDeSol/Nivel/CreateNivel', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          nombre: nivelName,
          requisitos: reqSel.map(req => req.id) }),
      });
      const data = await response.json();
      
     location.reload();      
     
    } catch (error) {
      console.error('Error al crear el nivel:', error);
    }
  };
  
    return (
      <div>
        <>
          <Link onPress={onOpen} color="success"  >
            Añadir Nivel
          </Link>
          <Modal
            backdrop="opaque" 
            isOpen={isOpen}
            onOpenChange={onOpenChange}
            placement="top-center"
            classNames={{
              backdrop: "bg-gradient-to-t from-zinc-900 to-zinc-900/10 backdrop-opacity-20"
            }}
          >
            <form onSubmit={handleSubmit}>
            <ModalContent>
           
              {(onClose) => (
                <>
                  <ModalHeader className="flex flex-col gap-1 ">
                    Añadir Nivel
                  </ModalHeader>
                  <ModalBody>
    
                  <Input
                      label="nombre del nivel"
                      type="text"
                      value={nivelName}
                      onChange={(e)=> setNivelName(e.target.value)}
                      className="max-w-xs w-full flex"
                      required
                      
                    />
                        <Select
      label="Requisitos"
      placeholder="Selecione los requisitos"
      onChange={(e)=> {
        const selectedIdsString = e.target.value;
    // Divide la cadena por coma para obtener un arreglo de IDs como cadenas
  const idsArrayAsString = selectedIdsString.split(',');
  // Convierte las cadenas de IDs a números
  const idsArrayAsNumbers = idsArrayAsString.map(id => Number(id.trim()));
    // Filtra los requisitos basándose en los IDs numéricos
  const requisitosFiltradosPorId = requisitos.filter(requisito => idsArrayAsNumbers.includes(requisito.id));
  

  // Guarda los requisitos filtrados en el estado
  setreqSel(requisitosFiltradosPorId);

        
       }}
      selectionMode="multiple"
      className="max-w-xs w-full flex  text-default-500 hover:text-default-900 transition-colors"
    >
      {requisitos.map((requisito) => (
        <SelectItem key={requisito.id}  value={requisito.id}
        >
          {requisito.nombre} 
          
        </SelectItem>
      ))}
    </Select>

                  </ModalBody>
                  <ModalFooter>
                    <Button color="danger" variant="flat" onClick={onClose}>
                      Cerrar
                    </Button>
                    <Button color="success" type="submit" onPress={onClose}>
                      Crear Nivel
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