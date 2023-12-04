import React, { useEffect ,useState} from 'react'
import api from '../../api';
import "./get.scss"
const Get = () => {

const [users, setUsers] = useState([]);

console.log(users);
const fetchUsers = async () => {
  const res = await api.get("/users/");
  setUsers(res.data);
};

useEffect(() => {
  fetchUsers();
}, []);

  return (
    <>
      <div className="get-body">
        <div className="container">
          <h3>Get method</h3>
          <table border={1}>
            <thead>
              <tr>
                <th>ID</th>
                <th>Full Name</th>
                <th>Email</th>
                <th>Designation</th>
                <th>Active</th>
              </tr>
            </thead>
            <tbody>
              {users &&
                users.map((user) => (
                  <tr key={user.id}>
                    <td>{user.id}</td>
                    <td>{user.fullname}</td>
                    <td>{user.email}</td>
                    <td>{user.designation}</td>
                    <td>{user.is_active ? "Active" : "Inactive"}</td>
                  </tr>
                ))}
            </tbody>
          </table>
        </div>
      </div>
    </>
  );
}

export default Get