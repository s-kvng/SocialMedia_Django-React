import axios from "axios";
import createAuthRefreshInterceptor from "axios-auth-refresh";
import { getAccessToken, getRefeshToken, getUser } from "../hooks/user.action";

//create an axios instance
const axoisService = axios.create({
  baseURL: "http://localhost:8000/api",
  headers: {
    "Content-Type": "application/json",
  },
});

//interceptors manipulate the request before been sent, by adding the access token to the header of the request
axoisService.interceptors.request.use(async (config) => {
  /* retrieving the access token from the localStorage and adding it to the headers of the request*/
  // const { access } = JSON.parse(localStorage.getItem("auth"));
  config.headers.Authorization = `Bearer ${getAccessToken()}`;

  return config;
});

axoisService.interceptors.response.use(
  (res) => Promise.resolve(res),
  (err) => Promise.resolve(err)
);

const refreshAuthLogic = async (failedRequest) => {
  // const { refresh } = JSON.parse(localStorage.getItem("auth"));

  return axios
    .post(
      "auth/refresh/",
      {
        refresh: getRefeshToken(),
      },
      {
        baseURL: "http://localhost:8000/api",
        // headers: {
        //   Authorization: `Bearer ${getRefeshToken}`,
        // },
      }
    )
    .then((resp) => {
      const { access } = resp.data;
      failedRequest.response.config.headers["authorization"] =
        "Bearer " + access;
      localStorage.setItem(
        "auth",
        JSON.stringify({ access, refresh: getRefeshToken(), user: getUser() })
      );
    })
    .catch(() => {
      localStorage.removeItem("auth");
    });
};

//sets up the authentication refresh interceptor
createAuthRefreshInterceptor(axoisService, refreshAuthLogic);

export function fetcher(url) {
  return axoisService.get(url).then((res) => {
    return res.data;
  });
}

export default axoisService;
