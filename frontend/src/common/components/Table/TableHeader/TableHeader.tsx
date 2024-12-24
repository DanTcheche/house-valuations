import { PropsWithChildren } from "react";

interface TableHeaderProps
  extends PropsWithChildren,
    React.ComponentPropsWithoutRef<"thead"> {}

export const TableHeader = ({ children, ...rest }: TableHeaderProps) => {
  return <thead {...rest}>{children}</thead>;
};
