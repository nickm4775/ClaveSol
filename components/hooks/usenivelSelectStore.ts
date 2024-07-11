// userStore.ts
import {create} from 'zustand';


interface Requisito{

    nombre:string;
    permanecer:boolean;
    subir:boolean;

}


interface Nivel {
    id: number;
    nombre: string;
    requisitos: Requisito[];
  }

  interface NivelState {
    nivelData: Nivel | null;
    setNivel: (nivelData: Nivel | null) => void;
  }
  
  export const usenivelSelectStore = create<NivelState>((set) => ({
    nivelData: null,
    setNivel: (nivelData) => set((state) => ({...state, nivelData })),
  }));