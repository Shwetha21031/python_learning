import React from "react";
import { Link } from "react-router-dom";
import "./nav.scss";
const NavBar = () => {
  return (
    <>
      <div className="nav">
        <ul>
          <div>
            <Link to={"/"}>Employee Management system</Link>
          </div>
        </ul>
      </div>
    </>
  );
};

export default NavBar;
