import "./App.css";
import NavBar from "./Components/NavBar/NavBar";
import Routers from "./Components/Routers/Routers";
import "./apps.scss"
import { ToastContainer } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";
function App() {
  return (
    <>
      <NavBar></NavBar>
      <Routers />
      <ToastContainer />
    </>
  );
}

export default App;
