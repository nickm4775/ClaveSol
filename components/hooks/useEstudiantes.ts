// src/store.js

import create from 'zustand';

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

  interface StoreState {
    students: Estudiante[];
    addStudent: (student: Estudiante) => void;
    removeStudent: (id: number) => void;
    setAllStudents: (students: Estudiante[]) => void;
  }
  
  export const useEstudianteStore = create<StoreState>((set) => ({
    students: [],
    addStudent: (student) =>
      set((state) => ({ students: [...state.students, student] })),
    removeStudent: (id) =>
      set((state) => ({ students: state.students.filter((student) => student.id!== id) })),
    setAllStudents: (students) =>
      set({ students }), // Sobrescribe el estado de estudiantes completamente
  }));