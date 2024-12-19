import { twMerge } from "tailwind-merge";

interface TableCellProps extends React.ComponentPropsWithoutRef<"td"> {
  key: number;
  text?: string;
}

export const TableCell = ({
  text,
  key,
  className,
  ...rest
}: TableCellProps) => {
  return (
    <td key={key} className={twMerge("py-3 px-6", className)} {...rest}>
      {text}
    </td>
  );
};
