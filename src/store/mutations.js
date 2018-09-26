export const productsFetched = (state, data) => {
  state.products = [ ...data ]
};

export const userFetched = (state, data) => {
  console.log('userFetched ->\t', data);
  data ? state.user = { ...data, isLoggedIn: false} : state.user = data
};
