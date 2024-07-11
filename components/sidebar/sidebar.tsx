import React, { useEffect, useState } from "react";
import { Sidebar } from "./sidebar.styles";
import { Avatar, Tooltip, Image } from "@nextui-org/react";
import { HomeIcon } from "../icons/sidebar/home-icon";
import { PaymentsIcon } from "../icons/sidebar/payments-icon";
import { BalanceIcon } from "../icons/sidebar/balance-icon";
import { AccountsIcon } from "../icons/sidebar/accounts-icon";
import { CustomersIcon } from "../icons/sidebar/customers-icon";
import { ProductsIcon } from "../icons/sidebar/products-icon";
import { ReportsIcon } from "../icons/sidebar/reports-icon";
import { SettingsIcon } from "../icons/sidebar/settings-icon";
import { CollapseItems } from "./collapse-items";
import { SidebarItem } from "./sidebar-item";
import { SidebarMenu } from "./sidebar-menu";
import { FilterIcon } from "../icons/sidebar/filter-icon";
import { useSidebarContext } from "../layout/layout-context";
import { ChangeLogIcon } from "../icons/sidebar/changelog-icon";
import { usePathname } from "next/navigation";
import { useRouter } from "next/navigation";
import { usenivelSelectStore } from "../hooks/usenivelSelectStore";




interface Requisito{
  nombre:string;
  permanecer:boolean;
  subir:boolean;

}

interface Nivel {
  nombre: string;
  requisitos: Requisito[];
}

export const SidebarWrapper = () => {
  const pathname = usePathname();
  const { collapsed, setCollapsed } = useSidebarContext();
  const routes = useRouter();
  const [levels, setLevels] = useState<Nivel[]>([]);
  const [levelNames, setLevelNames]= useState<string[]>([]);
  const{setNivel}=usenivelSelectStore();

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
  
  const handleLevelClick = (items: string[]): void => {
    
    // Busca el nivel por su nombre en la lista de niveles
    const selectedLevelName = items[0];
    const selectedLevel = levels.find(level => level.nombre === selectedLevelName);
  
    // Verifica si se encontró el nivel seleccionado
    if (selectedLevel) {
      // Pasa el nivel completo a setNivel para almacenarlo en usenivelSelectStore
      usenivelSelectStore.setState({ nivelData: selectedLevel});
      
      if (location.pathname!== '/nivel') {
        // Si no estás en la página de nivel, navega a ella
        routes.push('/nivel');
      } else {
        usenivelSelectStore.setState({ nivelData: selectedLevel});
        console.log("nivel nuevo",usenivelSelectStore.getState() );
      }
    } else {
      console.error('Nivel no encontrado:', levelNames);
   } };


  return (
    <aside className="h-screen z-[20] sticky top-0">
      {collapsed ? (
        <div className={Sidebar.Overlay()} onClick={setCollapsed} />
      ) : null}
      <div
        className={Sidebar({
          collapsed: collapsed,
        })}
      >
        <div className={Sidebar.Header()}>
          <Image src="/images/logo/logo.webp"
              alt="Logo"
              width={176}
              height={32}
               />
          
        </div>
        <div className="flex flex-col justify-between h-full">
          <div className={Sidebar.Body()}>
            <SidebarItem
              title="Home"
              icon={<HomeIcon />}
              isActive={pathname === "/"}
              href="/"
            />
            <SidebarMenu title="Main Menu">
              {/* <SidebarItem
                isActive={pathname === "/accounts"}
                title="Accounts"
                icon={<AccountsIcon />}
                href="accounts"
              />
              <SidebarItem
                isActive={pathname === "/payments"}
                title="Payments"
                icon={<PaymentsIcon />}
              /> */}
              
              <CollapseItems
                icon={<CustomersIcon />}
                items={levelNames}
                title="Niveles"
                onItemClick={handleLevelClick }
              />
              {/* <SidebarItem
                isActive={pathname === "/products"}
                title="Products"
                icon={<ProductsIcon />}
              />
              <SidebarItem
                isActive={pathname === "/reports"}
                title="Reports"
                icon={<ReportsIcon />}
              /> */}
            </SidebarMenu>

           
          </div>
          <div className={Sidebar.Footer()}>
            <Tooltip content={"Settings"} color="primary">
              <div className="max-w-fit">
                <SettingsIcon />
              </div>
            </Tooltip>
            <Tooltip content={"Adjustments"} color="primary">
              <div className="max-w-fit">
                <FilterIcon />
              </div>
            </Tooltip>
            <Tooltip content={"Profile"} color="primary">
              <Avatar
                src="https://i.pravatar.cc/150?u=a042581f4e29026704d"
                size="sm"
              />
            </Tooltip>
          </div>
        </div>
      </div>
    </aside>
  );
};
