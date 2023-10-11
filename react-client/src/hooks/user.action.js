import axios from "axios";
import { useNavigate } from "react-router-dom";

function useUserActions() {
  const navigate = useNavigate();
  const baseURL = "http://localhost:8000/api";

  return { login, logout };

  function login(data) {
    return axios.post(`${baseURL}/auth/login/`, data).then((res) => {
      //
      setUserData(res.data);
      navigate("/");
    });
    //
  }

  function logout() {
    localStorage.remove("auth");
    navigate("/login/");
  }
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

function getAccessToken() {
  const auth = localStorage.getItem("auth");
  return auth.access;
}

function getRefeshToken() {
  const auth = localStorage.getItem("auth");
  return auth.refresh;
}

function setUserData(data) {
  localStorage.setItem(
    "auth",
    JSON.stringify({
      access: data.access,
      refresh: data.refresh,
      user: data.user,
    })
  );
}

export { getUser, useUserActions, getAccessToken, getRefeshToken };
