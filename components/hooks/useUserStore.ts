// userStore.ts
import {create} from 'zustand';


interface UserAccount {
    email: string;
    first_name: string;
    last_name: string;
    is_active: boolean;
    is_staff: boolean;
    is_coordinador: boolean;
    is_admin: boolean;
    is_estudiante: boolean;
  }

interface UserState {
  userData: UserAccount| null ; // Puedes especificar una interfaz más detallada según tus necesidades
  setUser: (userData: UserAccount | null) => void;
}

export const useUserStore = create<UserState>((set) => ({
  userData: null,
  setUser: (userData) => set((state) => ({...state, userData })),
}));