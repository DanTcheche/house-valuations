import { useQuery } from "@tanstack/react-query";

import { PropertyInterface } from "@/interfaces/propertyInterface";
import { getHouseValuationsForAddress } from "@/api/houseValuations";

export const useGetHouseValuationsForAddress = (address: string) => {
  return useQuery<PropertyInterface[], Error>({
    queryKey: ["houseValuations", address],
    queryFn: () => getHouseValuationsForAddress(address),
    enabled: !!address,
  });
};
