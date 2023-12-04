import React from "react";
import { Route, Routes } from "react-router-dom";
import Post from "../Post/Post";
import Get from "../Get/Get";
import Delete from "../Delete/Delete";
import Put from "../Put/Put";
import Home from "../Home/Home"

const Routers = () => {
  return (
    <>
      <Routes>
        <Route path="/" element={<Home />}></Route>
        <Route path="/Post" element={<Post />}></Route>
        <Route path="/Get" element={<Get />}></Route>
        <Route path="/Delete" element={<Delete />}></Route>
        <Route path="/Put" element={<Put />}></Route>
      </Routes>
    </>
  );
};

export default Routers;
