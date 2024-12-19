import { PropsWithChildren } from "react";
import { twMerge } from "tailwind-merge";

interface TableRowProps
  extends PropsWithChildren,
    React.ComponentPropsWithoutRef<"tr"> {}

export const TableRow = ({ children, className, ...rest }: TableRowProps) => {
  return (
    <tr
      className={twMerge(
        "bg-gray-200 text-gray-600 capitalize text-sm leading-normal",
        className
      )}
      {...rest}
    >
      {children}
    </tr>
  );
};
