const realEstateUrl = "api/realestate/";
const columnDescriptionUrl = "api/columndescription";

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

function handleFormat(data) {
  return data.map((d) => d.fields);
}
