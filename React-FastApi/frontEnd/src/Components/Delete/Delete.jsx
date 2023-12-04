import React,{useState , useEffect} from "react";
import api from "../../api";
import './delete.scss'

const Delete = () => {
  const [user_id,setUserId] = useState(0);
  const [users, setUsers] = useState([]);

  const fetchUsers = async () => {
    const res = await api.get("/users/");
    setUsers(res.data);
  };  
  const user_with_id = users.filter((user) => user.id === user_id);

  useEffect(() => {
    fetchUsers();
  }, []);
  
  const handleDelete = (e) =>{
    e.preventDefault()
    api.delete(`/users/${user_id}`);
    alert("successfully deleted")
  }
  return (
    <>
      <div className="del-body">
        <div className="container">
          <h3>Delete user</h3>
          <div>
            <label htmlFor="user_id">Enter Id to delete</label>
            <input
              type="text"
              name="user_id"
              id="user_id"
              onChange={(e) => setUserId(Number(e.target.value))}
              value={user_id}
            />
          </div>
          {
            <div className="user-details-del">
              {user_with_id[0] ? (
                <>
                  <div className="del-user-details">
                      <h5>User Details</h5>
                  <p>{user_with_id[0]["fullname"]}</p>
                  <p>{user_with_id[0]["email"]}</p>
                  <p>{user_with_id[0]["designation"]}</p>
                  <p>{user_with_id[0]["is_active"]}</p>
                  </div>
                </>
              ) : (
                "no users with id"
              )}
            </div>
          }
          <button onClick={handleDelete} className="del-btn">Delete</button>
        </div>
      </div>
    </>
  );
};

export default Delete;
