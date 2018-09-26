export const productsFetched = (state, data) => {
  state.products = [ ...data ]
};

export const userFetched = (state, data) => {
  console.log('userFetched ->\t', data);
  data && data.user ? state.user = { ...data.user, token: data.token, isLoggedIn: false} : state.user = data
};
