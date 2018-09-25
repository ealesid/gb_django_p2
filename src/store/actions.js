const apiRoute = 'api/v1';

const getCookie = (name) => {
  let matches = document.cookie.match(
    new RegExp("(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
  ));
  return matches ? decodeURIComponent(matches[1]) : undefined;
};


export const fetchProducts = async ({commit, }) => {
  const response = await fetch(`${apiRoute}/products/`);
  commit('productsFetched', await response.json());
};

export const fetchUser = async ({commit, }, user) => {
  if (!!user) {
    const response = await fetch(`${apiRoute}/users/${user}/`);
    user = await response.json();
    if (user.email) {
      commit('userFetched', user)
    } else { commit('userFetched', null) }
  } else { commit('userFetched', null) }
};

export const getLoggedIn = async () => {
  console.log('getLoggedIn ->\t')
};

export const getRegisteredIn = async ({commit, }, user) => {
  let response = await fetch(`${apiRoute}/users/`, {
    method: 'post',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': getCookie('csrftoken'),
    },
    body: JSON.stringify(user),
  });
  response = await response.json();
  if (response.email) {
    commit('userFetched', response)
  }
  console.log('getRegisteredIn ->\t', response)
};
