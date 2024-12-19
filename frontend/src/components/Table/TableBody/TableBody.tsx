import { PropsWithChildren } from "react";
import { twMerge } from "tailwind-merge";

interface TableBodyProps
  extends PropsWithChildren,
    React.ComponentPropsWithoutRef<"tbody"> {}

export const TableBody = ({ children, className, ...rest }: TableBodyProps) => {
  return (
    <tbody
      className={twMerge("text-gray-600 text-sm font-light", className)}
      {...rest}
    >
      {children}
    </tbody>
  );
};
