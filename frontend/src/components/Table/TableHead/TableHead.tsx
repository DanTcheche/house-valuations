import { twMerge } from "tailwind-merge";

interface TableHeadProps extends React.ComponentPropsWithoutRef<"th"> {
  key: number | string;
  text?: string;
}

export const TableHead = ({
  text,
  key,
  className,
  ...rest
}: TableHeadProps) => {
  return (
    <th
      key={key}
      className={twMerge("py-3 px-6 text-left", className)}
      {...rest}
    >
      {text}
    </th>
  );
};
