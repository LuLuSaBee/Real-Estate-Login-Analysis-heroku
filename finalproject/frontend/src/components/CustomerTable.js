import React from "react";

export default function CustomerTable(props) {
  const { rows } = props;

  return (
    <table className='table'>
      <thead className='thead-light'>
        <tr>
          <th scope='col'>期數</th>
          <th scope='col'>期初金額</th>
          <th scope='col'>每期支付額</th>
          <th scope='col'>利息費用</th>
          <th scope='col'>本金償還</th>
          <th scope='col'>期末欠款</th>
        </tr>
      </thead>
      <tbody>
        {rows.map((data, index) => (
          <tr key={index}>
            <th scope='row'>{index}</th>
            {data.map((number, index) => (
              <td key={index}>
                {number.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",")}
              </td>
            ))}
          </tr>
        ))}
      </tbody>
    </table>
  );
}
