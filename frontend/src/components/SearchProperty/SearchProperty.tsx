import { Button } from "@/common/components/Button";
import { SearchBar } from "@/common/components/SearchBar";
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
          e.preventDefault(); // Prevent form submission
          handleSearchClick(); // Trigger search on submit
        }}
      >
        <SearchBar
          className="w-full"
          placeholder="Search by property address"
          isLoading={isLoading}
          value={address}
          setValue={setAddress}
        />
        <Button type="submit">Search</Button>
      </form>
      {isLoading && "Searching"}
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
