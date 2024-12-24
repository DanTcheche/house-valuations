import { twMerge } from "tailwind-merge";

interface TableCellProps extends React.ComponentPropsWithoutRef<"td"> {
  text?: string;
}

export const TableCell = ({ text, className, ...rest }: TableCellProps) => {
  return (
    <td className={twMerge("py-3 px-6", className)} {...rest}>
      {text}
    </td>
  );
};
