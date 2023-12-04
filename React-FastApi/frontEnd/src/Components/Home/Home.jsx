import React from "react";
import NavBar from "../NavBar/NavBar";
import {Link} from "react-router-dom"
import "./home.scss"
const Home = () => {
  return (
    <>
      <div className="body">
        <div className="btn-container">
          <Link to={"/Post"}>
            <button className="create-btn btn">Create Employee</button>
          </Link>
          <Link to={"/Get"}>
            <button className="view-btn btn">View Employees</button>
          </Link>
          <Link to={"/Put"}>
            <button className="update-btn btn">Update Employee</button>
          </Link>
          <Link to={"/Delete"}>
            <button className="delete-btn btn">Delete Employee</button>
          </Link>
        </div>
      </div>
    </>
  );
};

export default Home;
