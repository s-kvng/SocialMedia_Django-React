import React from "react";

import { Route, Routes } from "react-router-dom";

import ProtectedRoute from "./routes/ProtectedRoute";
import Home from "./pages/Home";
import "./App.css";

function App() {
  return (
    <Routes>
      <Route
        to="/"
        element={
          <ProtectedRoute>
            <Home />
          </ProtectedRoute>
        }
      />
      <Route path="/login/" element={<div>Login</div>} />
    </Routes>
  );
}

export default App;
