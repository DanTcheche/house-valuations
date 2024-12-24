import { Navigate, Route, Routes, useLocation } from "react-router-dom";
import type { Location } from "react-router-dom";
import { ROUTES } from "./routes";

import { Layout, Table } from "@/common/components";

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
          <Route element={<Table />} path={ROUTES.home} />
        </Route>
      </Routes>
    </>
  );
};
