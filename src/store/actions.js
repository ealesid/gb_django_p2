const apiRoute = 'api/v1';
let auth2;

const getCookie = (name) => {
  let matches = document.cookie.match(
    new RegExp("(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
  ));
  return matches ? decodeURIComponent(matches[1]) : undefined;
};

const attachSignin = (commit, element) => {
  console.log('attachSignin ->\t', element.id);
  auth2.attachClickHandler(element, {},
    function (googleUser) {
      // console.log('attachClickHandler ->\t', googleUser.getBasicProfile());
      document.getElementById('name').innerText = "Вы вошли как: " + googleUser.getBasicProfile().getName();
      // console.log('googleUser ->\t', googleUser.Zi.access_token, googleUser)
      fetchSocialUser(commit, googleUser.Zi.access_token);
      // commit('userFetched', {access_token: googleUser.Zi.access_token});
    },
    function (error) { console.log(JSON.stringify(error, undefined, 2)) });
};

export const startGoogleAuthApp = ({commit, state, }) => {
  gapi.load('auth2', function () {
    // Retrieve the singleton for the GoogleAuth library and set up the client.
    auth2 = gapi.auth2.init({
      client_id: state.client_id,
      cookiepolicy: 'single_host_origin',
      // Request scopes in addition to 'profile' and 'email'
      //scope: 'additional_scope'
    });
    attachSignin(commit, document.getElementById('customBtn'));
  });
};

export const fetchProducts = async ({commit, }) => {
  const response = await fetch(`${apiRoute}/products/`);
  commit('productsFetched', await response.json());
};

export const fetchUser = async ({commit, }, user) => {
  console.log('fetchUser ->\t', user);
  if (!!user) {
    const response = await fetch(`${apiRoute}/users/${user}/`);
    user = await response.json();
    if (user.email) {
      commit('userFetched', user)
    } else { commit('userFetched', null) }
  } else { commit('userFetched', null) }
};

export const fetchSocialUser = async(commit, token) => {
  let response = await fetch('/auth/google/', {
    method: 'post',
    headers: { 'Content-Type': 'application/json', },
    body: JSON.stringify({access_token: token}),
  });
  console.log('fetchSocialUser ->\t', token);
  console.log('fetchSocialUser ->\t', await response.json())
};

export const getLoggedIn = async () => {
  console.log('getLoggedIn ->\t')
};

export const getRegisteredIn = async ({commit, }, user) => {
  let response = await fetch(`/auth/registration/`, {
    method: 'post',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(user),
  });
  // let response = await fetch(`${apiRoute}/users/`, {
  //   method: 'post',
  //   headers: {
  //     'Content-Type': 'application/json',
  //     'X-CSRFToken': getCookie('csrftoken'),
  //   },
  //   body: JSON.stringify(user),
  // });
  if (response.ok) {
    response = await response.json();
    commit('userFetched', response)
  }
  console.log('getRegisteredIn ->\t', response)
};
