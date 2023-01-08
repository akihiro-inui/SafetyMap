// import { BrowserRouter as Router, Route } from 'react-router-dom';

import { BrowserRouter, Routes, Route } from "react-router-dom";
import React from 'react';
import CustomMap from './Components/Map/Map';


export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route exact path="/" element={<CustomMap/>}/>
      </Routes>
    </BrowserRouter>
  );
}
