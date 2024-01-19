import NextAuth from "next-auth";
import { InitOptions } from "next-auth";
import Providers from "next-auth/providers/index";
import { NextApiRequest, NextApiResponse } from "next";
import axios from "axios";

import { BASE_URL, SOCIAL_LOGIN_ENDPOINT, makeUrl } from "../../../urls";
import { AuthenticatedUser, CustomSessionObject } from "../../../types";
import { GenericObject } from "next-auth/_utils";

const settings: InitOptions = {
  providers: [
    Providers.Google({
      clientId: process.env.GOOGLE_CLIENT_ID,
      clientSecret: process.env.GOOGLE_CLIENT_SECRET,
      authorizationUrl:
        "https://accounts.google.com/o/oauth2/v2/auth?prompt=consent&access_type=offline&response_type=code",
    }),
  ],

  secret: process.env.NEXT_AUTH_SECRET,

  session: {
    maxAge: 6 * 60 * 60, // 6 hours
  },

  callbacks: {
    async signIn(user: AuthenticatedUser, account, profile) {
      if (account.provider === "google") {
        const { accessToken, idToken, provider } = account;
        user.accessToken = accessToken;
        user.idToken = idToken;
        user.provider = provider;
        return true;
      }

      return false;
    },

    async session(session: CustomSessionObject, user: AuthenticatedUser) {
      session.accessToken = user.accessToken;
      session.idToken = user.idToken;
      session.provider = user.provider;
      return session;
    },

    async jwt(token, user: AuthenticatedUser, account, profile, isNewUser) {
      if (user) {
        token.accessToken = user.accessToken;
        token.idToken = user.idToken;
        token.provider = user.provider;
      }

      return token;
    },
  },
};

export default (req: NextApiRequest, res: NextApiResponse) => {
  return NextAuth(req, res, settings);
};