import React, { useEffect } from "react";
import { signIn, signOut, useSession } from "next-auth/client";
import { Typography, Button, Box } from "@material-ui/core";
import { makeUrl, BASE_URL, SOCIAL_LOGIN_ENDPOINT } from "../urls";
import axios from "axios";
axios.defaults.withCredentials = true;

function index() {
  const [session, loading] = useSession();

  useEffect(() => {
    const getTokenFromServer = async () => {
      // TODO: handle error when the access token expires
      const response = await axios.post(
        // DRF backend endpoint, api/social/google/ for example
        // this returns accessToken and refresh_token in the form of HTTPOnly cookies
        makeUrl(BASE_URL, SOCIAL_LOGIN_ENDPOINT, session.provider),
        {
          access_token: session.accessToken,
          id_token: session.idToken,
        },
      );
    };

    if (session) {
      getTokenFromServer();
    }
  }, [session]);

  return (
    <React.Fragment>
      <Box
        display="flex"
        justifyContent="center"
        alignItems="center"
        m={5}
        p={5}
        flexDirection="column"
      >
        {!loading && !session && (
          <React.Fragment>
            <Typography variant="button">Not logged in</Typography>
            <Button
              variant="outlined"
              color="secondary"
              onClick={() => signIn()}
            >
              Login
            </Button>
          </React.Fragment>
        )}
        {!loading && session && (
          <React.Fragment>
            <Typography>Logged in as {session.user.email}</Typography>
            <pre>{JSON.stringify(session, null, 2)}</pre>
            <Button
              variant="outlined"
              color="primary"
              onClick={() => signOut()}
            >
              Sign Out
            </Button>
          </React.Fragment>
        )}
      </Box>
    </React.Fragment>
  );
}

export default index;