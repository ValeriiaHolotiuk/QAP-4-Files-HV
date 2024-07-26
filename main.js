import MotelCustomer from './customer.js';

// Example usage:
const mailingAddress = {
  street: "74 Goodridge St",
  city: "St.Johns",
  state: "NL",
  zip: "A1C2Y7"
};

const customer = new MotelCustomer(
  "Valeriia Holotiuk",
  "1999-03-22",
  "Feale",
  ["Non-Smoking", "King Bed"],
  "Credit Card",
  mailingAddress,
  "1111-111",
  "2024-07-20",
  "2024-07-28"
);

// Output the customer's description as HTML
document.body.innerHTML = customer.getDescription();