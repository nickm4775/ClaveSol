'use client'
import React from 'react';
import {  Card, Button } from '@nextui-org/react';
import Footer from "@/components/Home/footer";
import Hero from "@/components/Home/hero";
import Pricing from "@/components/Home//pricing";
import Partners from "@/components/Home/partners";
import Faq from "@/components/Home/faq";
import { useUserStore } from '@/components/hooks/useUserStore';

const Home: React.FC = () => {
  
   return (
      <>
     
    
    <div className="flex flex-col min-h-screen">
   <div>
   <main>
      
      <Hero />
      <Partners />
      <Pricing />
      <Faq />
    </main>
    <Footer />


   </div>
      
    </div>



     
      </>


)
};


 export default Home;
 