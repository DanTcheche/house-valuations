import { twMerge } from "tailwind-merge";

interface TableHeadProps extends React.ComponentPropsWithoutRef<"th"> {
  text?: string;
}

export const TableHead = ({ text, className, ...rest }: TableHeadProps) => {
  return (
    <th className={twMerge("py-3 px-6 text-left", className)} {...rest}>
      {text}
    </th>
  );
};
