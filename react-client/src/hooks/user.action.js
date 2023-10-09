import axios from "axios";
import { useNavigate } from "react-router-dom";

function useUserActions() {
  //   const navigate = useNavigate();
  //   const baseURL = "http://localhost:8000/api";
}

// Get the user
function getUser() {
  const auth = JSON.parse(localStorage.getItem("auth")) || null;
  if (auth) {
    return auth.user;
  } else {
    return null;
  }
}

export { getUser };
