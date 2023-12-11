import React, { useState } from "react";

const Loginpage = () => {
  const [showpwd, setShowpwd] = useState(false);
  const [userdetails, setUserDetails] = useState({
    username: "",
    password: "",
  });
  const [resetui, setResetui] = useState(true);
  const clearData = () => {
    setUserDetails({
      username: "",
      password: "",
    });
  };
  const handleLogin = () => {
    console.log(userdetails);
    clearData();
  };
  const handleResetPassword = () => {
    console.log("resetted password", userdetails);
    clearData();
  };

  return (
    <>
      {resetui ? (
        <div className="login-main">
          <div className="container">
            <h3>Login</h3>
            <div>
              <label for="username">Username</label>
              <input
                required
                value={userdetails.username}
                type="text"
                name="username"
                id="username"
                onChange={(e) =>
                  setUserDetails({ ...userdetails, username: e.target.value })
                }
              />
            </div>
            <div>
              <label for="password">Password</label>
              <input
                required
                value={userdetails.password}
                type={showpwd ? "text" : "password"}
                name="password"
                id="password"
                onChange={(e) =>
                  setUserDetails({ ...userdetails, password: e.target.value })
                }
              />
              <div className="show-btn">
                <label for="showpassword">Show password</label>
                <input
                  required
                  type="checkbox"
                  onClick={() => setShowpwd(!showpwd)}
                  name="showpassword"
                />
              </div>
            </div>
            <button onClick={handleLogin}>Login</button>

            <button
              onClick={() => {
                setResetui(false);
                clearData();
              }}
            >
              Reset Password
            </button>
          </div>
        </div>
      ) : (
        <div className="reset-main">
          <div className="container">
            <h3>Reset</h3>
            <div>
              <label for="username">Username</label>
              <input
                required
                value={userdetails.username}
                type="text"
                name="username"
                id="username"
                onChange={(e) =>
                  setUserDetails({ ...userdetails, username: e.target.value })
                }
              />
            </div>
            <div>
              <label for="password">Password</label>
              <input
                required
                value={userdetails.password}
                type={showpwd ? "text" : "password"}
                name="password"
                id="password"
                onChange={(e) =>
                  setUserDetails({ ...userdetails, password: e.target.value })
                }
              />
              <div className="show-btn">
              <label for="showpassword">Show password</label>
              <input
                required
                type="checkbox"
                onClick={() => setShowpwd(!showpwd)}
                name="showpassword"
              />
              </div>
            </div>
            <button
              onClick={() => {
                setResetui(true);
                clearData();
              }}
            >
              Cancel
            </button>
            <button onClick={handleResetPassword}>Reset Password</button>
          </div>
        </div>
      )}
    </>
  );
};

export default Loginpage;
