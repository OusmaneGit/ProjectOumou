import {Route, Routes,BrowserRouter} from "react-router-dom";
import MainWrapper from "./layouts/MainWrapper";
import PrivateRoute from "./layouts/PrivateRoute";
import ForgotPassword from "./views/auth/ForgotPassword";
import CreateNewPassword from "./views/auth/CreateNewPassword";

import Index from "./views/base/Index";
import Register from "../src/views/auth/Register";
import Login from "../src/views/auth/Login";
import Logout from "../src/views/auth/Login";
function App(){
  return (
    <BrowserRouter>
      <MainWrapper>
        <Routes>
          <Route  path="/register/" element={<Register />}/>
          <Route path="/login/" element ={<Login />}/>
          <Route path="/logout/" element ={<Logout />}/>
          <Route path="/forgot-password/" element={<ForgotPassword />} />
          <Route path="/create-new-password/" element={<CreateNewPassword />} />
          
                                      {/* Base Routes */}
          <Route path="/" element={<Index />} />

        </Routes>
      </MainWrapper>
    </BrowserRouter>
  )
}
export default App;