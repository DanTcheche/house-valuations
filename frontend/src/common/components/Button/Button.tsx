import { ComponentPropsWithoutRef, ForwardedRef, forwardRef } from "react";
import { twMerge } from "tailwind-merge";
import Spinner from "../Spinner/Spinner";

interface ButtonProps extends ComponentPropsWithoutRef<"button"> {
  isLoading?: boolean;
}

export const Button = forwardRef(
  (
    {
      type = "button",
      className,
      disabled = false,
      isLoading = false,
      children,
      ...props
    }: ButtonProps,
    ref: ForwardedRef<HTMLButtonElement>
  ) => (
    <button
      ref={ref}
      type={type}
      className={twMerge(
        "flex w-full items-center gap-2 rounded-md border border-transparent font-medium focus:outline-none focus:ring-2 focus:ring-offset-0",
        className
      )}
      disabled={disabled}
      {...props}
    >
      {isLoading ? <Spinner className="h-5 w-5" /> : <>{children}</>}
    </button>
  )
);
