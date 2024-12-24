import { ComponentPropsWithoutRef } from "react";
import { twMerge } from "tailwind-merge";
import Spinner from "../Spinner/Spinner";

interface SearchBarProps extends ComponentPropsWithoutRef<"input"> {
  setValue: (value: string) => void;
  value?: string;
  error?: string;
  isLoading?: boolean;
}

export const SearchBar = ({
  error,
  className,
  value,
  setValue,
  disabled,
  isLoading = false,
  ...props
}: SearchBarProps) => {
  const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) =>
    setValue(event.target.value);

  return (
    <div
      className={twMerge(
        "flex w-1/3 items-center justify-between rounded-lg border border-gray-200 bg-gray-50 px-3 font-light text-gray-600",
        className,
        error && "border-red-500 bg-red-50",
        value && "border-gray-400",
        disabled && "bg-gray-100"
      )}
    >
      <input
        className={twMerge(
          "h-11 w-full truncate rounded-md border-0 bg-transparent text-gray-700 placeholder:text-left focus:outline-none focus:ring-0",
          error && "text-red-700"
        )}
        id="search"
        {...props}
        disabled={disabled}
        type="text"
        value={value}
        onChange={handleInputChange}
      />
      {isLoading ? <Spinner className="size-4" /> : <></>}
    </div>
  );
};
