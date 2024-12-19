import { useOutlet } from "react-router-dom";

export const Layout = () => {
  const outlet = useOutlet();

  return (
    <div>
      <div>
        <main>{outlet}</main>
      </div>
    </div>
  );
};
