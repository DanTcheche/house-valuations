import { TableBody } from "../TableBody";
import { TableCell } from "../TableCell";
import { TableHead } from "../TableHead";
import { TableHeader } from "../TableHeader";
import { TableRow } from "../TableRow";

interface TableProps {
  data: any[];
}

export const Table = ({ data }: TableProps) => {
  const keys = Array.from(new Set(data.flatMap(Object.keys)));
  return (
    <div className="grid place-items-center overflow-x-auto">
      <table className="bg-white border border-gray-200">
        <TableHeader>
          <TableRow>
            <TableHead key={"header"} />
            {data.map((houseValuation) => (
              <TableHead
                key={houseValuation.id}
                text={houseValuation.provider}
              />
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
