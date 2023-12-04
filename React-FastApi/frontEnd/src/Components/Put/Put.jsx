import React from "react";
import { useEffect, useState } from "react";
import api from "../../api";
import "./put.scss"
const Put = () => {
  const [users, setUsers] = useState([]);
  const [formData, setFormData] = useState({
    fullname: "",
    email: "",
    designation: "",
    is_active: false,
  });
  const [user_id, setUserId] = useState();

  const fetchUsers = async () => {
    const res = await api.get("/users/");
    setUsers(res.data);
  };

  const user_with_id = users.filter((user) => user.id === user_id);

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
    try{
      api.put(`/users/${user_id}`,{...formData})
      .then(response=>{
        alert("Update Successful")
        })

    }catch{
      console.log("an error occured")
    }

   

    setFormData({
      fullname: "",
      email: "",
      designation: "",
      is_active: false,
    });


  };
  
  return (
    <>
      <div className="put-body">
        <form>
          <h3>Put Method</h3>
          <div className="input-elements">
            <div>
              <label htmlFor="user_id">Enter id to update</label>
              <input
                type="text"
                name="user_id"
                id="user_id"
                onChange={(e) => setUserId(Number(e.target.value))}
                value={user_id}
              />
            </div>

            {
              <div>
                {user_with_id[0] ? (
                  <>
                    <div className="user-details">
                      <h5>User Details</h5>
                      <p>{user_with_id[0]["fullname"]}</p>
                      <p>{user_with_id[0]["email"]}</p>
                      <p>{user_with_id[0]["designation"]}</p>
                      <p>{user_with_id[0]["is_active"]}</p>
                    </div>
                  </>
                ) : (
                  <span>No users found</span>
                )}
              </div>
            }

            <div>
              <label htmlFor="fullname">Full Name</label>
              <input
                type="text"
                name="fullname"
                id="fullname"
                onChange={handleinputChange}
                value={formData.fullname}
              />
            </div>
            <div>
              <label htmlFor="email">Email</label>
              <input
                type="text"
                name="email"
                id="email"
                onChange={handleinputChange}
                value={formData.email}
              />
            </div>
            <div>
              <label htmlFor="designation">Designation</label>
              <input
                type="text"
                name="designation"
                id="designation"
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

            <button
              type="submit"
              className="submit-btn"
              onClick={handleFormSubmit}
            >
              Submit
            </button>
          </div>
        </form>
      </div>
    </>
  );
};
export default Put;
