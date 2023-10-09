import React from "react";

import { Navigate } from "react-router-dom";
const ProtectedRoute = ({ children }) => {
  const { user } = JSON.parse(localStorage.getItem("auth"));
  return user ? <div>{children}</div> : <Navigate to={"/login/"} />;
};

export default ProtectedRoute;
