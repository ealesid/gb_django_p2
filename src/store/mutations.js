export const productsFetched = (state, data) => {
  state.products = [ ...data ]
};

export const userFetched = (state, data) => {
  state.user = data
};
