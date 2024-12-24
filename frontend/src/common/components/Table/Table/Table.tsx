import { TableBody } from "../TableBody";
import { TableCell } from "../TableCell";
import { TableHead } from "../TableHead";
import { TableHeader } from "../TableHeader";
import { TableRow } from "../TableRow";

const data = [
  { id: 1, name: "Item 1", amount: 100, description: "Description 1" },
  { id: 2, name: "Item 2", amount: 200 },
  { id: 3, name: "Item 3", amount: 300, notes: "Some notes" },
];

export const Table = () => {
  const keys = Array.from(new Set(data.flatMap(Object.keys)));
  return (
    <div className="grid place-items-center overflow-x-auto">
      <table className="bg-white border border-gray-200">
        <TableHeader>
          <TableRow>
            <TableHead key={"header"} />
            {data.map((provider) => (
              <TableHead key={provider.id} text={`Provider ${provider.id}`} />
            ))}
          </TableRow>
        </TableHeader>
        <TableBody>
          {keys.map((key) => (
            <TableRow key={key}>
              <TableHead key={key} text={key} />
              {data.map((provider) => (
                <TableCell
                  key={provider.id}
                  text={provider[key] ? provider[key] : "N/A"}
                />
              ))}
            </TableRow>
          ))}
        </TableBody>
      </table>
    </div>
  );
};

export default Table;
