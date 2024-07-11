"use client";
import { motion } from "framer-motion";
import { Tooltip } from "@nextui-org/tooltip";

export default function Partners() {
  return (
    <section className="max-w-screen-md mx-auto px-4 py-24 gap-12 md:px-8 flex flex-col justify-center items-center">
      <motion.h2
        initial={{ y: 5, opacity: 0 }}
        whileInView={{
          y: 0,
          opacity: 1,
        }}
        viewport={{ once: true }}
        transition={{ duration: 0.5 }}
        className="text-2xl font-bold sm:text-3xl bg-gradient-to-b from-foreground to-foreground/70 text-transparent bg-clip-text"
      >
        Usamos
      </motion.h2>
      <div className="w-full  gap-5 place-items-center">
       <motion.h6 initial={{ y: 5, opacity: 0 }}
        whileInView={{
          y: 0,
          opacity: 1,
        }}
        viewport={{ once: true }}
        transition={{ duration: 0.5 }}
        className=" font-bold  bg-gradient-to-b from-foreground to-foreground/70 text-transparent bg-clip-text"
     >
Usamos un sistema de niveles y recursos interactivos con tal de ubicarlo según sus habilidades para así lograr un aumento progresivo de capacidades  

       </motion.h6>
       
      </div>
    </section>
  );
}
