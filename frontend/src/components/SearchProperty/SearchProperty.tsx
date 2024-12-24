import { Button } from "@/common/components/Button";
import { SearchBar } from "@/common/components/SearchBar";
import Spinner from "@/common/components/Spinner/Spinner";
import { Table } from "@/common/components/Table";
import { useGetHouseValuationsForAddress } from "@/hooks/useGetHouseValuationsForAddress";
import { useState } from "react";

export const SearchProperty = () => {
  const [address, setAddress] = useState<string>("");
  const [searchAddress, setSearchAddress] = useState<string>("");
  const {
    data: propertyValuations,
    isLoading,
    isFetched,
  } = useGetHouseValuationsForAddress(searchAddress);

  const handleSearchClick = () => {
    if (address) {
      setSearchAddress(address);
    }
  };
  return (
    <>
      <form
        onSubmit={(e) => {
          e.preventDefault();
          handleSearchClick();
        }}
      >
        <div className="flex items-center justify-center w-full m-7">
          <SearchBar
            className="w-1/2 m-3"
            placeholder="Search by property address"
            isLoading={isLoading}
            value={address}
            setValue={setAddress}
          />
          <Button
            className="w-20 h-11 border border-gray-300 rounded-lg pl-3"
            type="submit"
            disabled={isLoading}
          >
            Search
          </Button>
        </div>
      </form>
      {isLoading && (
        <div className="flex items-center justify-center h-20 w-full">
          <Spinner className="h-10 w-10" />
        </div>
      )}
      {isFetched && propertyValuations ? (
        <Table data={propertyValuations} />
      ) : (
        ""
      )}
      {isFetched &&
        propertyValuations !== undefined &&
        !propertyValuations.length &&
        "No results found"}
    </>
  );
};
