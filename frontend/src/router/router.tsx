import { Navigate, Route, Routes, useLocation } from "react-router-dom";
import type { Location } from "react-router-dom";
import { ROUTES } from "./routes";
import { Layout } from "@/common/components/Layout";
import { SearchProperty } from "@/components/SearchProperty";

export const Router = () => {
  const location = useLocation();
  const { previousLocation } = (location.state ?? {}) as {
    previousLocation?: Location;
  };

  return (
    <>
      <Routes location={previousLocation ?? location}>
        <Route element={<Navigate to={ROUTES.home} />} path={"*"} />
        <Route element={<Layout />}>
          <Route element={<SearchProperty />} path={ROUTES.home} />
        </Route>
      </Routes>
    </>
  );
};
