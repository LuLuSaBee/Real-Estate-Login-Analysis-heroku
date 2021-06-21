const realEstateUrl = "api/realestate/";
const columnDescriptionUrl = "api/columndescription";
const totalValueUrl = "api/totalvalue";

export const getColumnDescription = (callback) => {
  fetch(columnDescriptionUrl)
    .then((res) => res.json())
    .then((result) => callback(handleFormat(result)))
    .catch((e) => console.log(e));
};

export const getRealEstate = (times, callback) => {
  fetch(realEstateUrl + times)
    .then((res) => res.json())
    .then((result) => callback(handleFormat(result)))
    .catch((e) => console.log(e));
};

export const getTotalValue = (callback) => {
  fetch(totalValueUrl)
    .then((res) => res.json())
    .then((result) => callback(handleFormat(result)))
    .catch((e) => console.log(e));
};

function handleFormat(data) {
  return data.map((d) => d.fields);
}
