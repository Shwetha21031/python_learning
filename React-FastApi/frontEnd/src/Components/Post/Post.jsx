import React, { useEffect, useState } from "react";
import api from "../../api";
import "./post.scss";
import {  toast } from "react-toastify";
const Post = () => {
  const [users, setUsers] = useState([]);
  const [formData, setFormData] = useState({
    fullname: "",
    email: "",
    designation: "",
    is_active: false,
  });

  const fetchUsers = async () => {
    const res = await api.get("/users/");
    setUsers(res.data);
  };

  useEffect(() => {
    fetchUsers();
  }, []);

  const handleinputChange = (e) => {
    const val =
      e.target.type === "checkbox" ? e.target.checked : e.target.value;
    setFormData({
      ...formData,
      [e.target.name]: val,
    });
  };

  const handleFormSubmit = async (e) => {
    e.preventDefault();
    await api.post("/users/", formData);
    fetchUsers();
    setFormData({
      fullname: "",
      email: "",
      designation: "",
      is_active: false,
    });
    toast.success("User Created Successfully!",{
      position:"top-right",
      autoClose:3000,
    });
  };
  return (
    <>
      <div className="post-body">
        <form>
          <h3>Post Method</h3>
          <div className="input-elements">
            <div>
              <label htmlFor="fullname">Full name</label>
              <br></br>
              <input
                type="text"
                name="fullname"
                id="fullname"
                onChange={handleinputChange}
                placeholder="Full name"
                value={formData.fullname}
                
              />
            </div>
            <div>
              <label htmlFor="email">Email</label> <br></br>
              <input
                type="text"
                name="email"
                id="email"
                placeholder="Email"
                onChange={handleinputChange}
                value={formData.email}
              />
            </div>
            <div>
              <label htmlFor="designation">Designation</label> <br></br>
              <input
                type="text"
                name="designation"
                id="designation"
                placeholder="Designation"
                onChange={handleinputChange}
                value={formData.designation}
              />
            </div>
            <div>
              <label htmlFor="is_active">Is active</label>
              <input
                type="checkbox"
                name="is_active"
                id="is_active"
                onChange={handleinputChange}
                value={formData.is_active}
              />
            </div>

            <button type="submit" onClick={handleFormSubmit} className="submit-btn">
              Submit
            </button>
          </div>
        </form>
      </div>
    </>
  );
};

export default Post;
