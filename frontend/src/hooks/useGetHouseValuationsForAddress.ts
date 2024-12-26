import { useQuery } from "@tanstack/react-query";
import { getHouseValuationsForAddress } from "@/api/houseValuations";
import { toast } from "react-toastify";
import { useEffect } from "react";

export const useGetHouseValuationsForAddress = (address: string) => {
  const { data, isLoading, isFetched, isError } = useQuery({
    queryFn: () => getHouseValuationsForAddress(address),
    queryKey: ["houseValuations", address],
    enabled: !!address,
    retry: false,
  });
  useEffect(() => {
    if (isError) {
      toast.error(
        "There was an error processing your request, please try again later."
      );
    }
  }, [isError]);
  return { data, isLoading, isFetched };
};
